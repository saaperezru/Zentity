$(function(){
  // Image Model
  // ----------
  window.Image = Backbone.Model.extend({
    defaults: function() {
      return {
        selected:  true,
        imgId: 0,
      };
    },
    toggle: function() {
      this.save({selected: !this.get("selected")});
    }
  });
  // Image Collection
  // ---------------
  window.ImageCollection = Backbone.Collection.extend({
    model: Image,
    localStorage: new Store("images"),
    selected: function() {
      return this.filter(function(image){ return image.get('selected'); });
    },
    remaining: function() {
      return this.without.apply(this, this.selected());
    },
  });
  window.Images = new ImageCollection;
  // Image Item View
  // --------------
  window.ImageView = Backbone.View.extend({
    tagName:  "li",
    template: _.template(
"<a class='<%= selected ? '' : 'deselected' %>'> \
  <img class=\"thumbnail\" height=\"40\" width=\"40\"></img> \
</a>"
    ),
    events: {
      "click img"   : "toggleSelected",
    },
    initialize: function() {
      this.model.bind('change', this.render, this);
      this.model.bind('destroy', this.remove, this);
    },
    render: function() {
      $(this.el).html(this.template(this.model.toJSON()));
      this.setImage();
      return this;
    },
    setImage: function(){
      this.$('img').attr("src","/images/get?id=" + this.model.get('imgId'));
    },
    toggleSelected: function() {
      $.ajax({
        url : "images/select?id=" + this.model.get("imgId") + "&s=" + this.model.get("selected"),
        success: function(response){
          if(response.error) {
            console.log(data.error);
          }
          this.$('img').toggleClass("loading");
          this.model.toggle();
        },
      });
    },
    remove: function() {
      $(this.el).remove();
    },
    clear: function() {
      this.model.destroy();
    }
  });

  // The Application
  // ---------------
  window.AppView = Backbone.View.extend({
    el : $('#imgapp'),
    statsTemplate : _.template(
"<% if (total) { %> \
  <span class=\"image-count\"> \
    <span class=\"number\"><%= selected %></span> \
    <span class=\"word\"><%= selected == 1 ? 'item' : 'items' %></span> selected. \
  </span> \
<% } %> \
<% if (remaining) { %> \
  <span class=\"image-clear\"> \
    <a href=\"#\"> \
      Clear <span class=\"number-deselected\"><%= remaining %></span> \
      deselected <span class=\"word-remaining\"><%= remaining == 1 ? 'item' : 'items' %></span> \
    </a> \
  </span> \
<% } %>"
    ),
    events : {
      "click #loadImages" : "createImages",
      "click .image-clear a": "clearDeselected",
    },
    initialize: function(){
      this.input    = document.getElementById("imageInput");

      Images.bind('add',   this.loadOne, this);
      Images.bind('reset', this.loadAll, this);
      Images.bind('all',   this.render, this);
      Images.fetch();
      if(window.Images.length === 0){
        this.createImages();
      }
    },
    render: function() {
      this.$('#image-stats').html(this.statsTemplate({
        total:      Images.length,
        selected:       Images.selected().length,
        remaining:  Images.remaining().length
      }));
    },
    loadOne :function(image) {
      var view = new ImageView({model:image});
      this.$('#image-list').append(view.render().el);
    },
    loadAll :function() {
      Images.each(this.loadOne)
    },
    createImages : function() {
      $.ajax({
        url : "/images/list",
        success: function(response){
          if(response.error) {
            console.log(data.error);
          }
          if(response.images) {
            console.log(response);
            _.each(response.images,function(image){
              Images.create({
                selected : image.selected,
                imgId : image.imgId,
              });
            });
          }
        }
      });
    },
    clearDeselected : function() {
      _.each(Images.remaining(), function(image){ image.destroy(); });
      return false;
    }
  });
  // Finally, we kick things off by creating the **App**.
  window.App = new AppView;
});
