// main.js

document.addEventListener('DOMContentLoaded', () => {
  const loadMoreBtn = document.querySelector('.load-more-btn');

  loadMoreBtn.addEventListener('click', () => {
    loadMoreBtn.innerText = 'Loading...';

    setTimeout(() => {
      // Simulate loading more posts (in a real app, this would be AJAX fetching)
      loadMoreBtn.innerText = 'Load More';
    }, 2000);
  });
});
