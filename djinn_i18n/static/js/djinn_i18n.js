$(document).ready(function() {

  $("[data-msgid]").each(function(idx, elt) {

    elt = $(elt);
    elt.css("position", "relative");

    elt.parent().on("contextmenu", function() {
      return false;
    });

    elt.parent().on("mousedown", function(e) { 

      if (e.button == 2) { 

        e.preventDefault();
        
        var tgt = $(e.currentTarget);
        
        if (!elt.find(".trans").length) {
          elt.append('<div class="trans hide"><a href="/i18n/trans/' + elt.data('msgid') + '/nl_NL/" class="modal-action">translate</a></div>');
        }
        
        $(".trans").hide();
        $(elt).find(".trans").show();
        
        return false;
      } 
    });
  });
});
