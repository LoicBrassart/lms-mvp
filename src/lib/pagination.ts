export const PAGE_SIZE = 10;

export function setupPagination(listId: string) {
  const items = document.querySelectorAll<HTMLLIElement>(`#${listId} > li`);
  const prevBtn = document.getElementById("prev-page") as HTMLButtonElement;
  const nextBtn = document.getElementById("next-page") as HTMLButtonElement;
  const pageIndicator = document.getElementById("page-indicator") as HTMLSpanElement;
  const pagination = document.getElementById("pagination") as HTMLDivElement;

  const totalPages = Math.ceil(items.length / PAGE_SIZE);

  if (totalPages <= 1) {
    pagination.hidden = true;
    return;
  }

  let currentPage = 0;

  function renderPage(page: number) {
    items.forEach((item, i) => {
      item.hidden = i < page * PAGE_SIZE || i >= (page + 1) * PAGE_SIZE;
    });
    prevBtn.disabled = page === 0;
    nextBtn.disabled = page === totalPages - 1;
    pageIndicator.textContent = `Page ${page + 1} / ${totalPages}`;
  }

  prevBtn.addEventListener("click", () => {
    currentPage--;
    renderPage(currentPage);
  });
  nextBtn.addEventListener("click", () => {
    currentPage++;
    renderPage(currentPage);
  });

  renderPage(0);
}
