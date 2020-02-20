$(document).ready(function(){

    const allSitesCount = parseInt($('#allSitesCount').text());
    const sitesTable = $('#sitesTable');
    const sitesTableError = $('#sitesTableError');
    const sites = 'http://127.0.0.1:5000/sites';
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
            beforeSend: function() {
                
            },
            success: function(response) {
                response.map(function(site) {
                    getStatus(site);
                });
            }
        });
    }

    function getStatus(site){
        $.ajax({
            url: site,
            method: 'GET',
            success: function(data, textStatus, xhr) {
                appendResult(sitesTable, 'success', site, xhr.status);
            },
            error: function(xhr, ajaxOptions, thrownError){
                console.log(xhr.status)
                appendResult(sitesTableError, 'danger', site, xhr.status);
            }
        });
    }

    function appendResult(tbody, trColor, url, status){
        tbody.append(
            `<tr class="tr-background-${trColor}">
                <td><a href="${url}" target="_blank">${url}</a></td>
                <td class="">${status}</td>
            </tr>`
        );
        increaseLoading(status);
    }

    verify.click(function() {
        getSites(sites);
    });




  
});