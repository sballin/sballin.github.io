<!-- {"full_title": "Space usage at Columbia"} -->

# Tracking space usage at Columbia <a href="https://github.com/sballin/rho_t"><i class="fa fa-github"></i></a>

During the last finals week of my junior year, an interesting website came online at [density.adicu.com](http://density.adicu.com/). It tracks the number of devices connected to WiFi access points at many places on campus, and translates these numbers into a crowdedness metric (100% := full, 0% := empty). The website, however, only shows the crowdedness at the instant you access it. ρ(t) is a tool I made while procrastinating during finals week that scrapes data from the website every 15 minutes and shows it using a D3 plot. It's not a smart solution now since there's an API, but it can show you how to scrape a website.

<center><a href="http://www.columbia.edu/~sbb2151/rho_t/"><img src="{{top-path}}/{{article-path}}/finals.jpg"/></a></center>

Above is what ρ(t) recorded during finals at Columbia. The largest fluctuations are between daytime and nighttime (although a fair number of people stay active at Butler, the 24-hour library). We can also see on most days a swell in activity after lunchtime. In my experience, finding a spot in the library was impossible just after lunch.

And we also see the beautiful, gradual death of finals week over three days.

<!--  -->

If I were to remake this today, I would also probably use Chart.js:

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

