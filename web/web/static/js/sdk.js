(function() {
    let host = 'http://localhost:8001';
    let portalId = document.currentScript.dataset.id;

    let style = document.createElement('link');
    style.rel = 'stylesheet';
    style.href = host + '/static/css/sdk.css'
    document.head.appendChild(style);

    const request = new XMLHttpRequest();
    request.open("GET", host + "/api/portals/"+portalId);

    function create_weblet_card(title, img_url, created_by, created_on) {
       let lwCard = document.createElement('div');
       lwCard.classList.add('lw-card');

       let lwImg = document.createElement('img');
       lwImg.src = host + img_url;
       lwImg.alt = '';

       lwCardBody = document.createElement('div');
       lwCardBody.classList.add('card-body');

       lwCardTitle = document.createElement('div');
       lwCardTitle.classList.add('title');
       if (title.length > 20)
           title = title.slice(0, 25) + ' ...';
       lwCardTitle.textContent = title;

       lwCardMeta = document.createElement('div');
       lwCardMeta.classList.add('meta');
       if (created_by.length > 24)
           created_by = created_by.slice(0, 26) + ' ...';
       lwCardMeta.innerHTML = `<span style="margin-bottom: 0.5rem;">- by ${created_by}</span><span>- on ${created_on}</span>`;

       lwCardBody.append(lwCardTitle);
       lwCardBody.append(lwCardMeta);

       lwCard.append(lwImg);
       lwCard.append(lwCardBody);

       return lwCard;

    }

    request.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           const response = JSON.parse(this.responseText);
           let lwContainer = document.getElementById('lw-portals-container');
           response['weblets'].forEach(function(weblet) {
               let lwCard = create_weblet_card(weblet.title, weblet.img_url, weblet.created_by, weblet.created_on)
               lwContainer.append(lwCard);
           })
       }
    };

    request.send();

})();
