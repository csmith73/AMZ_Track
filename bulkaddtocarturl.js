
console.log('Other sellers page found....');
numSellers = document.querySelectorAll('.olpOffer').length;
console.log(numSellers);
var offers = []
$('div.olpPriceColumn').each(function() {
    var $this = $(this);
    var offerId = $('input[name="offeringID.1"]', $this.closest('.olpOffer')).val();
    if (offerId != '') {
        offers.push({'offerListingId' : offerId});
        console.log(offers);
        urlIndex = i + 1
        urlIndex = urlIndex.toString()
        cartUrl = cartUrl + 'OfferListingId.' + urlIndex + '=' + offerId + '&Quantity.' + urlIndex + '=100&'
        console.log(cartUrl)
    }
});

for(i=0;i<numSellers;i++){
    sellerName = document.getElementsByClassName('a-spacing-none olpSellerName')[i].textContent;
    sellerName = sellerName.replace(/\s/g, '');
    sellerNameArray.push(sellerName);
    console.log(sellerNameArray);

    // offerId = document.getElementsByName("offeringID.1")[i].value;
    // urlIndex = i + 1
    // urlIndex = urlIndex.toString()
    // cartUrl = cartUrl + 'OfferListingId.' + urlIndex + '=' + offerId + '&Quantity.' + urlIndex + '=100&'
    // console.log(cartUrl)
}



