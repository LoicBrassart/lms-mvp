export const PAGE_SIZE = 10;

export interface PaginationElements {
  pagination: HTMLElement;
  prevBtn: HTMLButtonElement;
  nextBtn: HTMLButtonElement;
  pageIndicator: HTMLSpanElement;
}

export function getPaginationElements(): PaginationElements | null {
  const pagination = document.getElementById("pagination");
  const prevBtn = document.getElementById("prev-page");
  const nextBtn = document.getElementById("next-page");
  const pageIndicator = document.getElementById("page-indicator");

  if (!pagination || !prevBtn || !nextBtn || !pageIndicator) return null;

  return {
    pagination,
    prevBtn: prevBtn as HTMLButtonElement,
    nextBtn: nextBtn as HTMLButtonElement,
    pageIndicator: pageIndicator as HTMLSpanElement,
  };
}

export function updatePaginationControls(
  page: number,
  totalPages: number,
  els: PaginationElements,
) {
  if (totalPages > 1) {
    els.pagination.hidden = false;
    els.prevBtn.disabled = page === 0;
    els.nextBtn.disabled = page === totalPages - 1;
    els.pageIndicator.textContent = `Page ${page + 1} / ${totalPages}`;
  } else {
    els.pagination.hidden = true;
  }
}

export function setupPagination(listId: string) {
  const items = document.querySelectorAll<HTMLLIElement>(`#${listId} > li`);
  const els = getPaginationElements();
  if (!els) return;

  const totalPages = Math.ceil(items.length / PAGE_SIZE);

  if (totalPages <= 1) {
    els.pagination.hidden = true;
    return;
  }

  let currentPage = 0;

  function renderPage(page: number) {
    items.forEach((item, i) => {
      item.hidden = i < page * PAGE_SIZE || i >= (page + 1) * PAGE_SIZE;
    });
    updatePaginationControls(page, totalPages, els);
  }

  els.prevBtn.addEventListener("click", () => {
    currentPage--;
    renderPage(currentPage);
  });
  els.nextBtn.addEventListener("click", () => {
    currentPage++;
    renderPage(currentPage);
  });

  renderPage(0);
}
