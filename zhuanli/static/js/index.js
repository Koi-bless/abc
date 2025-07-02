$(function(){
    $('dl:first>dd').addClass('focus')
    $('dd')
        .addClass('no-focus')
        .click(function(){
            $('dd').removeClass('focus');
            $(this).addClass('focus');
            $('iframe').attr('src', $(this).attr('href'))
    });

    $('iframe').attr('src', '/patent_list')
});