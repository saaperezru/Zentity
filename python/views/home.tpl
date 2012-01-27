<html>
    <head>
        <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
        <style type="text/css">
            body {
                padding-top: 60px;
            }
        </style>
    </head>
    <body>
        <div class="topbar">
            <div class="topbar-inner">
                <div class="container-fluid">
                    <a class="brand" href="#">MODELADO</a>
                </div>
            </div>
        </div>
        <div class="container-fluid">
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
        <form method="post" action="/home" enctype="multipart/form-data">
        <!--- GENERAL MATRICES -->
        <div class="page-header">
            <h1>General Matrices</h1>
            <small>FALTA INSTRUCCIONES.</small>
        </div>
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend>Original Term Documents Matrices</legend>
                  <label for="fileInput">File input</label>
                  <div class="input">
                    <input class="input-file" id="fileInput" name="TermDocumentMatrix" type="text" value="../matlab/matrix/TD.mat">
                  </div>
                  <label for="">Variable Name</label>
                  <div class="input">
                    <input class="xlarge" id="xlInput" name="TermDocumentMatrixName" size="30" type="text" value="TD">
                  </div>
                </fieldset>
              </div>
              <div class="span4">
                <fieldset>
                  <legend>Documents list</legend>
                  <label for="fileInput">File input</label>
                  <div class="input">
                    <input class="input-file" id="DocumentsList" name="fileInput" type="text">
                  </div><!-- /clearfix -->
                  <label for="">Variable Name</label>
                  <div class="input">
                    <input class="xlarge" id="xlInput" name="DocumentsListName" size="30" type="text">
                  </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- /row -->
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend>Textual features list </legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="fileInput" name="TextualFeaturesList" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="TextualFeaturesListName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
              <div class="span8">
                <fieldset>
                  <legend>Documents images path</legend>
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="DocumentsPath" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- row -->
         <!--- TEXTUAL CLUSTERING MATRICES -->
        <div class="page-header">
            <h1>Textual Clustering Matrices</h1>
            <small>FALTA INSTRUCCIONES.</small>
        </div>
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend> Textual Basis Matrix (Ft) </legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="fileInput" name="TextualF" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="TextualFName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
              <div class="span8">
                <fieldset>
                  <legend>General Textual Representation Matrix (H)</legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="xlInput" name="TextualH" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="TextualHName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- /row -->
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend> Visual Basis from Textual Clustering (FTv) </legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="fileInput" name="TextualVisualF" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="TextualVisualFName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- /row -->
        <!--- VISUAL CLUSTERING MATRICES -->
        <div class="page-header">
            <h1>Visual Clustering Matrices</h1>
            <small>FALTA INSTRUCCIONES.</small>
        </div>
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend> Visual Basis Matrix (Ft) </legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="fileInput" name="VisualF" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="VisualFName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
              <div class="span8">
                <fieldset>
                  <legend>General Visual Representation Matrix (H)</legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="xlInput" name="VisualH" type="text">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="VisualHName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- /row -->
        <div class="row">
              <div class="span8">
                <fieldset>
                  <legend> Visual Basis from Textual Clustering (FTv) </legend>
                           <div class="clearfix">
                            <label for="fileInput">File input</label>
                            <div class="input">
                              <input class="input-file" id="fileInput" name="VisualTextualF" type="file">
                            </div>
                          </div><!-- /clearfix -->
                          <div class="clearfix">
                            <label for="">Variable Name</label>
                            <div class="input">
                              <input class="xlarge" id="xlInput" name="VisualTextualFName" size="30" type="text">
                            </div>
                          </div><!-- /clearfix -->
                </fieldset>
              </div>
        </div><!-- /row -->
        <div class="actions">
            <input type="submit" class="btn primary" value="Save changes">&nbsp;<button type="reset" class="btn">Cancel</button>
        </div>
        
        </form>
        </div><!-- /content-well -->
        <footer>
            <p>&copy; Company 2011</p>
        </footer>
    </body>
</html>
