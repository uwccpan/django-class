const mainEl=document.getElementById("main");
console.log(mainEl);

let charts = echarts.init(mainEl);

console.log(charts);

$(document).ready(() => {
    $.ajax(
        {
            url:'/pm25-data',
            type:"POST",
            dataType: "json",
            success:(datas)=>{
                //指定圖表的配置項和資料
            const option = {
                title: {
                    text: "PM25",
                },
                tooltip: {},
                legend: {
                    data: ["PM2.5"],
                },
                xAxis: {
                    data: datas['sites'],
                },
                yAxis: {},
                series: [
                    {
                        name: "銷量",
                        type: "bar",
                        data: datas['values'],
                        itemStyle: {
                            color: '#a90000'
                          }
                    },
                ],
            };

            charts.setOption(option);

            }
        }
    )
});

