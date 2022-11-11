/* 
Function to populate a standard header
*/
function populateHeader(header) {
  header.innerHTML = (
    `
<h1><a href="index">Iuncterra</a></h1>
<h3 class=sub><a class=ipa>iʌŋktɛræ</a></h3>

<nav>
    <a href="locations">Locations</a>
    <a href="organisations">Organisations</a>
    <a href="cosmology">Cosmology</a>
    <a href="species">Species'</a>
    <a href="people">People</a>
    
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
Function to create a contents page. 

Any header (h1, h2, h3, h4, h5 or h6) is included if it has a value for `.id`, headers are sorted by level (h1 > h2 > h3 > etc.)
*/
function buildContentsBox(contents) {
  // Do nothing if no page marked as contents
  if (contents === undefined) {
    return
  }

  /* 
  * Iterative function to get subheaders
  */
  function addSubnodes(parentHeader, parentNode) {
    // Get level of parent
    let lvl = parseInt(parentHeader.tagName.replace("H", ""));
    // List sibling headers
    let currentSibling = parentHeader;
    let finished = false;
    while (!finished) {
      // Get next sibling
      currentSibling = currentSibling.nextElementSibling;
      if (!currentSibling) {
        // If sibling is blank, finished
        finished = true;
      } else if (!["H1", "H2", "H3", "H4", "H5", "H6"].includes(currentSibling.tagName)) {
        // If sibling isn't a heading, next sibling
      } else {
        // Work out its level
        siblingLvl = parseInt(currentSibling.tagName.replace("H", ""));
        if (siblingLvl && siblingLvl <= lvl) {
          // If its level is g/e to parent header, finished
          finished = true;
        } else if (currentSibling.id) {
          // If it's a header with an ID, add node for this header
          item = addNode(currentSibling, parentNode);
          // Also add any children
          currentSibling = addSubnodes(currentSibling, item).previousElementSibling;
        }
      }
    }

    return currentSibling
  }

  /*
  * Add node for given heading
  */
  function addNode(header, parentNode) {
    // Create link to id
    let link = document.createElement("a");
    link.href = `#${header.id}`;
    parentNode.appendChild(link);
    // Get text content of title (without suffixes)
    let item = document.createElement("li");
    item.textContent = Array.prototype.filter.call(header.childNodes, function (element) {
      return element.nodeType === Node.TEXT_NODE;
    }).map(function (element) {
      return element.textContent;
    }).join("");
    // Add item text to link
    link.appendChild(item)

    return item;
  }

  // Create header
  let header = document.createElement("h4");
  header.textContent = "Contents";
  contents.appendChild(header);
  // Add h1 nodes
  let thisItem;
  for (let header of document.getElementsByTagName("H1")) {
    // Skip page header
    if (header.parentElement.id === "home-page-header") {
      continue;
    }
    // Add node
    thisItem = addNode(header, contents)
    // Iteratively add child nodes
    addSubnodes(header, thisItem)
  }
}

/*
* Add a link to IPA reader to any IPA pronunciation string.
*/
function linkIPA(obj) {
  obj.href = `http://ipa-reader.xyz/?text=${obj.textContent}&voice=Brian`
}


/*
Master function calling all other populate functions
*/
function populateAll() {
  // Populate header
  populateHeader(document.getElementById("home-page-header"));
  populateFooter(document.getElementById("home-page-footer"));
  buildContentsBox(document.getElementById("contents"));
  for (let obj of document.getElementsByClassName("ipa")) {
    linkIPA(obj)
  }
}

// Bind to window load event
window.onload = populateAll
