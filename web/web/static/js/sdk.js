(function() {
    let BASE_URL = 'http://localhost:8001/';
    let weblets = [
        {
            'img_url': BASE_URL + 'media/weblets/Webinar%20by%20Abhinav%20Kumar/thumbnail/preview_4.png',
            'title': 'Why IoT is so hot',
            'created_by': 'abhinav.kumar',
            'created_on': new Date()
        },
        {
            'img_url': BASE_URL + 'media/weblets/Why%20IoT%20is%20so%20hot/thumbnail/preview_1_xkCKW60.png',
            'title': 'Webinar by Abhinav',
            'created_by': 'abhinav.kumar',
            'created_on': new Date()
        },
        {
            'img_url': BASE_URL + 'media/weblets/Weblet%20by%20Richa%20Ahuja/thumbnail/preview_2_ffF9HBD.png',
            'title': 'Webinar by Sunil',
            'created_by': 'sunil.madan',
            'created_on': new Date()
        },
        {
            'img_url': BASE_URL + 'media/weblets/Binary%20Search%20tree/thumbnail/preview_3.png',
            'title': 'Webinar by Richa',
            'created_by': 'richa.ahuja',
            'created_on': new Date()
        },

    ];

    var css = document.createElement('link');
    css.href = BASE_URL + 'static/css/sdk.css';
    css.rel = 'stylesheet';
    document.getElementsByTagName('head')[0].appendChild(css);

    let root_ele = document.getElementById('lw-root');
    
    let container_ele = document.createElement('div');
    container_ele.setAttribute('class', 'container');
    root_ele.appendChild(container_ele);

    let col_ele = document.createElement('div');
    col_ele.setAttribute('class', 'col');
    container_ele.appendChild(col_ele);

    weblets.forEach(function(r) {
        let card = document.createElement('div');
        card.setAttribute('class', 'card');

        let card_img = document.createElement('img');
        card_img.setAttribute('src', r.img_url);
        card_img.setAttribute('class', 'card-img-top');
        card.appendChild(card_img);

        let card_body = document.createElement('div');
        card_body.setAttribute('class', 'card-body');
        card.appendChild(card_body);

        let card_title = document.createElement('h4');
        card_title.setAttribute('class', 'card-title');
        card_title.innerText = r.title;
        card_body.appendChild(card_title);

        col_ele.appendChild(card);
    })

})();
