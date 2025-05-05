/* chart.js – dashboard */
document.addEventListener("DOMContentLoaded", () => {

    // helpers
    const parseJSON = (id) => JSON.parse(document.getElementById(id)?.textContent || "{}");

    /* ---------- Doughnut statut ---------- */
    const st = parseJSON("jsonStatus");
    new Chart(
        document.getElementById("chartStatus"), {
            type: "doughnut",
            data: { labels: st.labels, datasets:[{ data: st.values }] },
            options: { plugins:{ legend:{ position:"bottom" } } }
        }
    );

    /* ---------- Line livres finis / mois ---------- */
    const mo = parseJSON("jsonMonthly");
    new Chart(
        document.getElementById("chartMonthly"), {
            type: "line",
            data: { labels: mo.labels, datasets:[{ data: mo.values, tension:.3, fill:true }] },
            options:{
                scales:{ y:{ beginAtZero:true, precision:0 } },
                plugins:{ legend:{ display:false } }
            }
        }
    );
});
