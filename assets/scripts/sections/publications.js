import Filterizr from 'filterizr'

document.addEventListener('DOMContentLoaded', () => {
  const publicationCardHolder = document.getElementById('publication-card-holder')
  if (publicationCardHolder != null && publicationCardHolder.children.length !== 0) {
    // eslint-disable-next-line no-new
    new Filterizr('.filtr-publications', {
      layout: 'sameWidth',
      gridItemsSelector: '.pub-filtr-item',
      controlsSelector: '.pub-filtr-control',
      // Lets the type filter (data-filter) and the year filter
      // (data-multifilter) apply at the same time instead of one
      // replacing the other.
      multifilterLogicalOperator: 'and',
    })
  }
})
