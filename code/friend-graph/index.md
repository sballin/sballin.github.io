# Friend graph <a href="https://github.com/sballin/friend_graph"><i class="fa fa-github"></i></a>

This is a tool to make a force-directed graph of your Facebook friend network. Each friend is represented as a node, and is connected to each of your mutual friends. Each time you load this page, friends are connected by springs, and they pull each other together in a physical simulation that results in a final balance. Highly connected groups pull each other close and will end up the way you group your friends in your mind: clustered around schools, towns, events, and organizations. This is what my friend network looks like:

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

It's more illuminating to look at the results excluding yourself as the central node that's connected to all others, because you know that already.

The biggest group I see is my high school. That's closely connected to a couple other clusters, including my college friends at Columbia and friends I met during a high school research program at Stony Brook University. Some clusters farther out aren't connected as well to the massive high school and college group. My friends from middle school in Vienna are in one such cluster. At the farthest outskirts, there are a few friends that aren't connected to the rest at all (other than through me). They correspond to about 1.5% of the total, which is tiny.

I wonder if Facebook uses an approach like this to recommend people for you to add as friends. At Facebook's scale, though, it's probably some heuristic that looks at connectivity up to 2 degrees of separation.
