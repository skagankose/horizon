$(document).ready(function() {

    $('#buttonSearch').on('click', function() {

        $.ajax( {

            type: "POST",
            url: "/userSearch/",
            data: {
                    'textSearch' : $('#userSearch').val(),
                    csrfmiddlewaretoken: $('#csrftoken').val()
            },
            success: function SearchSuccess(data, textStatus, jqXHR) {
                     $('#results').html(data);
            },
            dataType: 'html'
        });
    });
});


$(document).ready(function() {

    $('#buttonSearchV2').on('click', function() {

      $.ajax( {

          type: "POST",
          url: "/userSearchV2/",
          data: {
                  'textSearch' : $('#userSearchV2').val(),
                  csrfmiddlewaretoken: $('#csrftoken').val()
          },
          success: function SearchSuccess(data, textStatus, jqXHR) {
                   $('#results').html(data);
          },
          dataType: 'html'
      });
  });
});

$(document).ready(function() {

    $('#buttonSearchV3').on('click', function() {

      $.ajax( {

          type: "POST",
          url: "/addTogether/",
          data: {
                  csrfmiddlewaretoken: $('#csrftoken').val()
          },
          success: function SearchSuccess(data, textStatus, jqXHR) {
                   $('#results').html(data);
          },
          dataType: 'html'
      });
  });
});
