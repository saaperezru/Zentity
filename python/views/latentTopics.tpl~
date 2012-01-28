<!DOCTYPE html>
<html>
  <head>
    <title>Modelado</title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
    <script src="/static/jquery.min.js"></script>
    <script src="/static/underscore-1.1.6.js"></script>
    <script src="/static/json2.js"></script>
    <script src="/static/backbone.js"></script>
    <script src="/static/backbone-localstorage.js"></script>
    <script src="./static/latent.js"></script>
    <style type="text/css">
       div.notice{
         padding:5px !important;
       }
       div.innertopic{
         padding:10px;
         background:#fff;
         border-radius:4px;
         margin: 0px;
       }
      .topbar {
        position: static;
        margin-bottom: 20px;
      }
      .content{
        min-height:300px;
      }
      a.deselected{
       /* background :url( "http://cdn2.iconfinder.com/data/icons/bnw/128x128/apps/x.png");*/
        background-color: #666;
        background-size: cover;
        z-index: -99999;
      }
      img.wrapper    {
        opacity : 0.4;
        filter: alpha(opacity=40); // msie
        background-color: #000; 
      }
    </style>
  </head>
  <body>
    <!--
    -topbar
    -->
    <div class="topbar">
      <div class="topbar-inner">
        <div class="container-fluid">
          <a class="brand" href="#">MODELADO</a>
        </div>
      </div>
    </div>
    <!--
    -image app
    -->
    <div class="container-fluid" id="lapp">
      <div class="sidebar">
        <a href="/"><button class="offset1 btn span4"> HOME </button></a>
        <hr>
        <a href="/images"><button class="offset1 btn span4"> IMAGES </button></a>
        <hr>
        <a href="/latentTopics"><button class="offset1 btn span4 primary"> LATENT TOPICS </button></a>
        <hr>
        <a href="/latentTopics"><button class="offset1 btn span4"> CODE GENERATION </button></a>
      </div>
      <div class="content well">
        <div class="page-header">
          <h1>Select Latent Topics</h1>
        </div>
        <ul id="topic-list" class="unstyled">
        </ul>
        <div id="topic-stats">
        </div>
      </div>
      <footer>
      <p>&copy; copyleft 2011</p>
      </footer>
    </div>

  </body>
</html>
