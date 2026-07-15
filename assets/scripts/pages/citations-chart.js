import Chart from 'chart.js/auto'

const canvas = document.getElementById('citations-chart')
const dataEl = document.getElementById('citations-data')

if (canvas && dataEl) {
  const citationsByYear = JSON.parse(dataEl.textContent)
  const years = Object.keys(citationsByYear)
  const counts = Object.values(citationsByYear)

  new Chart(canvas, {
    type: 'bar',
    data: {
      labels: years,
      datasets: [
        {
          label: 'Citations',
          data: counts,
          backgroundColor: '#248aaa',
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        y: { beginAtZero: true, ticks: { precision: 0 } },
      },
    },
  })
}
