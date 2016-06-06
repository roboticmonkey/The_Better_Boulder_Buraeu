"use strict";

//ctx is the context aka. the location in the dom the chart goes
//jQuery short hand for document.ready()
$(function() {
    $.get("/get_chart_info.json", {"boulder_id":$("#bar_chart").data("boulder")}, createChart);
    
    function createChart(results){
        // if there is no data hide the div the shows the chart
        // or else do the shit below
        
        var ctx = $("#route_rating");
        var data = {
                labels: results['chart_labels'],
                datasets: [
                    {
                        label: "Route Rating Breakdown",
                        backgroundColor: "rgba(0, 204, 163,0.2)",
                        borderColor: "rgba(0, 204, 163,1)",
                        borderWidth: 1,
                        hoverBackgroundColor: "rgba(0, 204, 163,0.4)",
                        hoverBorderColor: "rgba(0, 204, 163,1)",
                        data: results['data'],
                        xAxesID: "Rating Scale",
                        yAxesID: "",
                    }
                ]
            };
        var options = {
            // responsive: false,
            responsive: true,

            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                        stepSize: 1,
                    }
                }]
            }


        }
        // console.log(results['chart_labels']);
        // console.log(results['data']);
        var barChart = new Chart(ctx, {
            type: "bar",
            data: data,
            options: options,
        });


    }
    
});


