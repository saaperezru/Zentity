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
        <div class="page-header">
            <h1>Load Matrices</h1>
            <p>FALTA INSTRUCCIONES.</p>
        </div>
        <div class="row">
            <h2>Load textual matrices</h2>
            <!-- HT-->
            <form><fieldset>
                <legend>Representation matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="TermDocumentMatrix" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input style="height:20px" class="xlarge" id="xlInput" name="TermDocumentMatrixName" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <!-- FT-->
            <form><fieldset>
                <legend>Basis matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <!-- FTV-->
            <form><fieldset>
                <legend>asymmetric Basis Matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <h2>Load visual matrices</h2>
            <!-- HV-->
            <form><fieldset>
                <legend>Representation matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <!-- FV-->
            <form><fieldset>
                <legend>Basis matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <!-- FVT-->
            <form><fieldset>
                <legend>asymmetric Basis Matrix</legend>
                <div class="row">
                    <div class="span6">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                    <div class="span6">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </div>     
            </fieldset></form>
            <h2>Load matrices</h2>
            <!-- Textual world matrix -->
            <div class="row">
                <form><fieldset>
                    <legend>Textual words matrix</legend>
                    <div class="clearfix">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                </fieldset></form>
            </div>
            <!-- Documents id-->
            <div class="row">
                <form><fieldset>
                    <legend>Documents id</legend>
                    <div class="clearfix">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                </fieldset></form>
            </div>
            <div class="row">
                <form><fieldset>
                    <legend>Tags matrix</legend>
                    <div class="clearfix">
                        <label for="fileInput">File input</label>
                        <div class="input">
                            <input type="file" name="fileInput" id="fileInput" class="input-file">
                        </div>
                    </div>
                </fieldset></form>
            </div>
            <div class="row">
                <form><fieldset>
                    <legend>Images path</legend>
                    <div class="clearfix">
                        <label for="xlInput">Variable name</label>
                        <div class="input">
                            <input tyle="height:20px" class="xlarge" id="xlInput" name="xlInput" size="40" type="text">
                        </div>
                    </div>
                </fieldset></form>
            </div>
        </div>
        <footer>
            <p>&copy; Company 2011</p>
        </footer>
    </body>
</html>
