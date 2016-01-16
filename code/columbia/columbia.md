# Columbia 

_Tools for life at Columbia._

## Space usage

<script src="Chart.js"></script>
<div style="width:100%">
    <div>
        <canvas id="canvas" height="200" width="600"></canvas>
    </div>
</div>
<script>
function getJSONP(url, success) {
    var ud = '_' + +new Date,
        script = document.createElement('script'),
        head = document.getElementsByTagName('head')[0] 
               || document.documentElement;
    window[ud] = function(data) {
        head.removeChild(script);
        success && success(data);
    };
    script.src = url.replace('callback=?', 'callback=' + ud);
    head.appendChild(script);
}

var dajson; 
getJSONP('http://density.adicu.com/day/2015-11-24/building/75?auth_token=RQ1Y4T3GVPP8QU0Q6LXXS5OY1CE9K8NY', function(data){
    console.log(data);
}); 
        var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
        var lineChartData = {
            labels : ["January","February","March","April","May","June","July"],
            datasets : [
                {
                    label: "My First dataset",
                    fillColor : "rgba(220,220,220,0.2)",
                    strokeColor : "rgba(220,220,220,1)",
                    pointColor : "rgba(220,220,220,1)",
                    pointStrokeColor : "#fff",
                    pointHighlightFill : "#fff",
                    pointHighlightStroke : "rgba(220,220,220,1)",
                    data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
                },
                {
                    label: "My Second dataset",
                    fillColor : "rgba(151,187,205,0.2)",
                    strokeColor : "rgba(151,187,205,1)",
                    pointColor : "rgba(151,187,205,1)",
                    pointStrokeColor : "#fff",
                    pointHighlightFill : "#fff",
                    pointHighlightStroke : "rgba(151,187,205,1)",
                    data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
                }
            ]

        }

    window.onload = function(){
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myLine = new Chart(ctx).Line(lineChartData, {
            responsive: true
        });
    }
</script>

## Old stuff

<center><a href="http://www.columbia.edu/~sbb2151/rho_t/"><img src="https://raw.githubusercontent.com/sballin/rho_t/master/finals.jpg"/></a></center>

ρ(t), so named because I am a physics nerd, scrapes data from [density.adicu.com](http://density.adicu.com/) every 15 minutes and shows it all using a D3 graph. Here's its [Github page](https://github.com/sballin/rho_t). It's useless now because Density made an API, but it can show you how to scrape a website.
