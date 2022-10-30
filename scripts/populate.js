/* 
Function to populate a standard header
*/
function populateHeader(header) {
  header.innerHTML = (
    `
<h1><a href="index.html">Iuncterra</a></h1>
<h3 class=sub><a class=ipa>iʌŋktɛræ</a></h3>

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
      // Get text content of title (without suffixes)
      item.textContent = Array.prototype.filter.call(pageInfo['title'].childNodes, function (element) {
        return element.nodeType === Node.TEXT_NODE;
      }).map(function (element) {
        return element.textContent;
      }).join("")

      link.appendChild(item);
    }
  }
}

function populateIPA() {
  for (let obj of document.getElementsByClassName("ipa")) {
    obj.href = `http://ipa-reader.xyz/?text=${obj.textContent}&voice=Brian`
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
  populateIPA()
}

// Bind to window load event
window.onload = populateAll
