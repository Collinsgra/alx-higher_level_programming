$(document).ready(() => {
    $('div#add_item').click(() => {
      $('ul.my_list').append('<li>Item</li>');
    });
    $('div#remove_item').click(() => {
      $('ul.my_list li')[0].remove();
    });
    $('div#clear_list').click(() => {
      $('ul.my_list li').remove();
    });
});  
