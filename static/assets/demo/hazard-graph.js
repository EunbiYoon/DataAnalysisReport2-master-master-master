// Global parameters:
// do not resize the chart canvas when its container does (keep at 600x400px)
// Chart.defaults.global.responsive = false;
// define the chart data
var chartData = {
    labels: JSON.parse(HjinjaLabels),
    
    datasets: [
      {
        data: JSON.parse(Hjinja0MValues),
        label: Hjinja0MLegend,
        borderColor:"#FF6E8C",
        backgroundColor:['rgba(227,98,125,0.2)'],
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "red",
        pointRadius: 1,
        pointHitRadius: 10
      },
      {
        data: JSON.parse(Hjinja1MValues),
        label: Hjinja1MLegend,
        backgroundColor:['rgba(86,176,238,0.2)'],
        borderColor:"#42A7EC",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "#42A7EC",
        pointRadius: 1,
        pointHitRadius: 10
      },
      {
        data: JSON.parse(Hjinja2MValues),
        label: Hjinja2MLegend,
        borderColor:"grey",
        backgroundColor:['rgba(122,122,122,0.2)'],
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "grey",
        pointRadius: 1,
        pointHitRadius: 10
      }]
  };
  
  console.log(HjinjaLabels);
  console.log(Hjinja2MValues);
  console.log(Hjinja1MValues);
  console.log(Hjinja0MValues);
  
  
  
  // get chart canvas
  var ctx = document.getElementById("hazardgraph").getContext("2d");
  
  // create the chart using the chart canvas
  var areachart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: {
      scales: {
        xAxes: [{
          type: 'category'
        }],
        y: {
          type: 'logarithmic',
          beginAtZero: true
        }
      }
    },
    // animation: {
    //   onComplete: function () {
    //     var chartInstance = this.chart;
    //     var ctx = chartInstance.ctx;
    //     ctx.textAlign = "center";
    //     ctx.font = "20px Arial";
    //     ctx.fillStyle = "white";                            
    //     Chart.helpers.each(this.data.datasets.forEach(function (dataset, i) {
    //       var meta = chartInstance.controller.getDatasetMeta(i);
    //       Chart.helpers.each(meta.data.forEach(function (bar, index) {
    //         if (chartInstance.data.datasets[i].data[index] !== 0) {
    //           ctx.save();
    //           ctx.translate(bar._model.x - 10, bar._model.y - 19);
    //           ctx.rotate(-0.5 * Math.PI);
    //           ctx.fillText(dataset.data[index], 0, 0);
    //           ctx.restore();
    //         }
    //       }),this)
    //     }),this);
    //   }
    // }
    
  });
  