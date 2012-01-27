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
    <script src="./static/images.js"></script>
    <style type="text/css">
      .topbar {
        position: static;
        margin-bottom: 20px;
      }
      .content{
        min-height:300px;
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
    <div class="container-fluid" id="imgapp">
      <div class="sidebar">
        <button class="offset1 btn span4 primary"> HOME </button>
        <hr>
        <button class="offset1 btn span4"> IMAGES </button>
        <hr>
        <button class="offset1 btn span4"> LATENT TOPICS </button>
        <hr>
        <button class="offset1 btn span4"> CODE GENERATION </button>
      </div>
      <div class="content well">
        <div class="page-header">
          <h1>Load Matrices</h1>
        </div>
        <div class="row">
          <form action="" method="get" accept-charset="utf-8" class="form-stacked">
            <label>insert a directory path to load images</label>
            <input type="text" name="dir" id="imageInput" class="xlInput" size="60">
            <input type="button" id="loadImages" value="Load" class="btn primary">
          </form>
        </div>
        <ul id="image-list" class="media-grid">
        </ul>
        <div id="image-stats">
        </div>
      </div>
      <footer>
      <p>&copy; copyleft 2011</p>
      </footer>
    </div>

  </body>
</html>
