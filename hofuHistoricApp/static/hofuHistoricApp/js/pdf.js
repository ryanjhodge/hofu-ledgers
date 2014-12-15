var page, system, address, output;
// Create a page object
page = require('webpage').create();
// Require the system module so I can read the command line arguments
system = require('system');
// Read the url and output file location from the command line argument
address = system.args[1];
output = system.args[2]
// Set the page size and orientation
page.paperSize = {
	format: 'letter',
	orientation: 'landscape',
	margin: '0.5in'
};
// Now we have everything settled, let's render the page
page.open(address, function (status) {
	if (status !== 'success') {
		// If PhantomJS failed to reach the address, print a message
		console.log('Unable to load the address!');
		phantom.exit();
	} 
	else {
		// If we are here, it means we rendered page successfully
		page.render(output);
		phantom.exit();
	}
});