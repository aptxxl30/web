function filteritem() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const items = document.querySelectorAll('.item');

    items.forEach(item => {
        const itemName = item.getAttribute('data-name').toLowerCase();
        if (item.includes(searchInput)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}
