$(function(){
  // Topic Model
  // ----------
  window.Topic = Backbone.Model.extend({
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
  // Topic Collection
  // ---------------
  window.TopicCollection = Backbone.Collection.extend({
    model: Topic,
    localStorage: new Store("topics"),
    selected: function() {
      return this.filter(function(topic){ return topic.get('selected'); });
    },
    remaining: function() {
      return this.without.apply(this, this.selected());
    },
  });
  window.Topics = new TopicCollection;
  // Topic Item View
  // --------------
  window.TopicView = Backbone.View.extend({
    tagName:  "li",
    template: _.template(
"<div class=\"notice alert-message block-message <%= selected ? 'success' : 'warning' %>\"> \
  <div class=\"innertopic row\"> \
    <h2><%= name %> <small><%= type %></small></h2> \
    <ul class=\"media-grid\"> \
    <% _.each(docs, function(img) { %> <li><a><img class='thumbnail' src='/images/get?id=<%= img %>'></a></li> <% }); %> \
    </ul> \
    <div class=\"clearfix\"></div> \
    <div class='input-prepend'> \
    <small> select </small><input type=\"checkbox\"  <%= selected ? 'checked' : '' %>/> \
    </div> \
  </div> \
</div>"
    ),
    events: {
      "click input"   : "toggleSelected",
    },
    initialize: function() {
      this.model.bind('change', this.render, this);
      this.model.bind('destroy', this.remove, this);
    },
    render: function() {
      $(this.el).html(this.template(this.model.toJSON()));
      return this;
    },
    toggleSelected: function() {
      var model = this.model;
      $.ajax({
        url : "/latentTopics/select?id=" + this.model.get("lid") + "&s=" + !this.model.get("selected") + "&type=" + this.model.get("type"),
        success: function(response){
          if(response.error) {
            console.log(data.error);
          }
          model.toggle();
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
    el : $('#lapp'),
    events : {
    },
    initialize: function(){
      Topics.bind('add',   this.loadOne, this);
      Topics.bind('reset', this.loadAll, this);
      Topics.bind('all',   this.render, this);
      this.createTopics();
    },
    render: function() {
    },
    loadOne :function(topic) {
      var view = new TopicView({model:topic});
      this.$('#topic-list').append(view.render().el);
    },
    loadAll :function() {
      Topics.each(this.loadOne)
    },
    createTopics : function() {
      $.ajax({
        url : "/latentTopics/list",
        success: function(response){
          if(response.error) {
            console.log(data.error);
          }
          if(response.LTS) {
            console.log(response);
            _.each(response.LTS,function(topic){
              Topics.create({
                selected : topic.selected,
                lid : topic.lid,
                type : topic.type,
                docs : topic.docs,
                name : topic.name,
              });
            });
          }
        }
      });
    },
  });
  // Finally, we kick things off by creating the **App**.
  window.App = new AppView;
});
