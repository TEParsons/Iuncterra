/* 
Function to populate a standard header
*/
function populateHeader(header) {
    header.innerHTML = (
`
<h1><a href="index.html">Iuncterra</a></h1>
<h3 class=sub><a href="http://ipa-reader.xyz/?text=iʌŋktɛræ&voice=Brian" class=ipa>iʌŋktɛræ</a></h3>

<nav>
    <a href="locations.html">Locations</a>
    <a href="organisations.html">Organisations</a>
    <a href="people.html">People</a>
    <a href="species.html">Species'</a>
</nav>
`
    )
}

/*
Function to populate footer
*/
function populateFooter(footer) {
    footer.innerHTML = (
`
Content: <a href="https://github.com/TEParsons">Todd Parsons</a></br>
Wiki Template: <a href="https://github.com/TEParsons">Todd Parsons</a></br>
Background: <a href="https://www.pexels.com/photo/dry-leaf-on-concrete-surface-5947472/">Eva Bronzini via Pexels</a>
`
    )
}

/*
Function to create a contents page
*/
function populateContentsPage(contents) {
  // Do nothing if no page marked as contents
  if (contents === undefined) {
    return
  }
  // Create header
  let header = document.createElement("h4");
  header.textContent = "Contents";
  contents.appendChild(header);
  // Add each page which has an id
  let pageInfo = {};
  let item;
  let link;
  for (let page of document.getElementsByClassName("wiki-page")) {
    // Get page info
    pageInfo['id'] = page.id;
    pageInfo['title'] = page.querySelector("h1");
      if (pageInfo['id'] && pageInfo['title']) {
        // If we have the minimum needed, make a list item
        link = document.createElement("a");
        link.href = `#${page.id}`;
        contents.appendChild(link);
        item = document.createElement("li");
        item.textContent = pageInfo['title'].textContent;
        link.appendChild(item);
    }
  }
}


/*
Master function calling all other populate functions
*/
function populateAll() {
    // Populate header
    populateHeader(document.getElementById("home-page-header"));
    populateFooter(document.getElementById("home-page-footer"));
    populateContentsPage(document.getElementById("contents"));
    
}

// Bind to window load event
window.onload = populateAll
