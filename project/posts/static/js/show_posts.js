obj = new Vue({
    el: '#show_posts',
    delimiters: ["[[", "]]"],
    methods: {
        read(post_id) {
            $.ajax({
                type: 'GET',
                async: false,
                url: url_read + post_id,
                success: function(data) {
                    if (data['status'] == "Read added")
                        document.getElementById('post' + post_id).innerHTML = '\
                        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-file-check-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> \
                        <path fill-rule="evenodd" d="M12 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm-1.146 6.854a.5.5 0 0 0-.708-.708L7.5 8.793 6.354 7.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/> \
                        </svg>';
                    else
                        document.getElementById('post' + post_id).innerHTML = '<svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-file-check" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> \
                        <path fill-rule="evenodd" d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm0 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H4z"/> \
                        <path fill-rule="evenodd" d="M10.854 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 8.793l2.646-2.647a.5.5 0 0 1 .708 0z"/> \
                        </svg>';              
                },
                dataType: 'json',
            });
        },
    }
    });