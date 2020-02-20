$(document).ready(function(){

    const allSitesCount = parseInt($('#allSitesCount').text());
    const sitesTable = $('#sitesTable');
    const sitesTableError = $('#sitesTableError');
    const sites = 'https://ideal-status.herokuapp.com/sites';
    const okSitesCount = $('#okSitesCount');
    const errorSitesCount = $('#errorSitesCount');
    const verify = $('#verify');
    const progressBar = $('progress');

    let sitesCount = 0;
    let sitesError = 0;
    let sitesOk = 0;

    
    $("#buscar").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".table tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    function increaseLoading(status){
        sitesCount++;
        if(status == 200) {
            sitesOk++;
            okSitesCount.text(sitesOk);
        }else{
            sitesError++;
            errorSitesCount.text(sitesError);
        }
        progressBar.val(sitesCount*100/allSitesCount);
    }

    function getSites(sites){
        $.ajax({
            url: sites,
            method: 'GET',
            success: function(response) {
                response.map(function(site) {
                    getStatus(site);
                });
            }
        });
    }

    function getStatus(site){
        $.ajax({
            url: `http://${site}`,
            method: 'GET',
            dataType: 'jsonp',
            success: function(data, textStatus, xhr) {
                appendResult(site, xhr.status);
            },
            error: function(xhr, ajaxOptions, thrownError){
                console.log(xhr.status)
                appendResult(site, xhr.status);
            }
        });
    }

    function appendResult(url, status){
        if (status == 200){
            trColor = 'success';
            tbody = sitesTable;
        }else{
            trColor = 'danger';
            tbody = sitesTableError;
        }
        tbody.append(
            `<tr class="tr-background-${trColor}">
                <td><a href="http://${url}" target="_blank">${url}</a></td>
                <td class="">${status}</td>
            </tr>`
        );
        increaseLoading(status);
    }

    verify.click(function() {
        getSites(sites);
    });




  
});