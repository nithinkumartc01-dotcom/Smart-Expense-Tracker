document.addEventListener('DOMContentLoaded', function() {
    // Only run if charts exist on page
    const categoryCtx = document.getElementById('categoryChart');
    const trendCtx = document.getElementById('trendChart');

    // Use dynamic data from backend if available, otherwise use placeholders
    const data = window.chartData || {
        categoryLabels: ['Food', 'Transport', 'Utilities', 'Entertainment'],
        categoryData: [300, 150, 100, 80],
        trendLabels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        trendData: [12, 19, 3, 5, 2, 3, 15]
    };

    if (categoryCtx) {
        new Chart(categoryCtx, {
            type: 'doughnut',
            data: {  
                labels: data.categoryLabels,
                datasets: [{
                    data: data.categoryData,
                    backgroundColor: ['#2563eb', '#3b82f6', '#60a5fa', '#93c5fd'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'bottom' },
                    title: { display: true, text: 'Expenses by Category' }
                }
            }
        });
    }

    if (trendCtx) {
        new Chart(trendCtx, {
            type: 'bar',
            data: {
                labels: data.trendLabels,
                datasets: [{
                    label: 'Daily Spending',
                    data: data.trendData,
                    backgroundColor: '#2563eb',
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true, grid: { display: false } },
                    x: { grid: { display: false } }
                }
            }
        });
    }
});