from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Document, Group, Message
from .forms import DocumentUploadForm, GroupForm, DocumentEditForm
# views.py
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentUploadForm, DocumentEditForm

def document_editor(request, doc_id=None):
    document = None
    if doc_id:
        # Editing an existing document
        document = Document.objects.get(id=doc_id)
        edit_form = DocumentEditForm(instance=document)
    else:
        # If no doc_id is provided, create a new document
        document = Document(name="New Document", content="")
        edit_form = DocumentEditForm(instance=document)

    if request.method == 'POST':
        if 'upload' in request.POST:
            # Handle document upload
            upload_form = DocumentUploadForm(request.POST)
            if upload_form.is_valid():
                # Save the uploaded document
                document = upload_form.save()
                return redirect('document_editor', doc_id=document.id)
        elif 'edit' in request.POST:
            # Handle document editing
            edit_form = DocumentEditForm(request.POST, instance=document)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('document_editor', doc_id=document.id)

    else:
        upload_form = DocumentUploadForm()

    return render(request, 'collaboration/document_editor.html', {
        'upload_form': upload_form,
        'edit_form': edit_form,
        'document': document,
    })

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    messages = group.messages.all()
    return render(request, 'collaboration/group_chat.html', {'group': group, 'messages': messages})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            form.save_m2m()
            return redirect('group_chat', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'collaboration/create_group.html', {'form': form})
