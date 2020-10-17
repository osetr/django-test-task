obj = new Vue({
    el: '#show_blogs',
    delimiters: ["[[", "]]"],
    methods: {
        like(blog_id) {
            $.ajax({
                type: 'GET',
                async: false,
                url: url_like + blog_id,
                success: function(data) {
                    document.getElementById('like' + blog_id + '_amount').innerHTML=data['likes_amount'];
                    if (data['status'] == "Like added")
                        document.getElementById('like' + blog_id).setAttribute("fill", "purple");
                    else
                        document.getElementById('like' + blog_id).setAttribute("fill", "gray");
                },
                dataType: 'json',
            });
        },
    }
    });