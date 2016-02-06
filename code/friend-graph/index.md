# Friend Graph <a href="https://github.com/sballin/friend_graph"><i class="fa fa-github"></i></a>

A graph of your Facebook friends. Below is what my network looks like. See the [project page on Github](https://github.com/sballin/friend_graph) for more info and make one of your own!

<thing width="700" height="700"></thing>

<script src="http://d3js.org/d3.v2.js?2.9.6"></script>
<script>

var width = 700,
    height = 700;

var canvas = d3.select("thing").append("canvas")
    .attr("width", width)
    .attr("height", height);

var force = d3.layout.force()
    .size([width, height]);

d3.json("friends.json", function(graph) {
  var context = canvas.node().getContext("2d");

  force
      .size([width, height])
      .nodes(graph.nodes)
      .links(graph.links)
      .gravity([.3])
      .on("tick", tick)
      .start();

  function tick() {
    context.clearRect(0, 0, width, height);

    // draw links
    context.strokeStyle = "#ccc";
    context.beginPath();
    graph.links.forEach(function(d) {
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(d.target.x, d.target.y);
    });
    context.stroke();

    // draw nodes
    context.fillStyle = "steelblue";
    context.beginPath();
    graph.nodes.forEach(function(d) {
      context.moveTo(d.x, d.y);
      context.arc(d.x, d.y, 2, 0, 2 * Math.PI);
    });
    context.fill();
  }
});

</script>

<!-- <center><iframe width="650" height="500" frameborder="0" border-color="#000" src="../../friends"/></center> -->
