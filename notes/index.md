Notes
=====

This page lets me paste stuff to the internet immediately using SimpleNote.

<div id="note"></div>

<script type="text/javascript" src="{{top-path}}jquery-2.1.4.min.js"></script>

<script type="text/javascript">
$('#note').load('http://cors.io/?u=https://app.simplenote.com/publish/53gczb#published_content', function() {
    var orig = document.getElementById("note").innerHTML;
    document.getElementById("note").innerHTML = orig.replace('<p>Public</p>', '').replace('<div class="published-top"><span class="logo"><a href="/" title="Get Simplenote">Published with Simplenote</a></span></div></div><!-- .published-wrap -->', '');
});
</script>
