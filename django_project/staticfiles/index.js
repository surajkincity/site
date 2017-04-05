Array.prototype.map.call(document.querySelectorAll('.tools a:not([data-role="createLink"])'), (action) => {
  action.addEventListener("click", (e) => {
    e.preventDefault();
    document.execCommand(action.dataset.role, false, action.dataset.value);
  })
})

// Handle the link modal
const modal = document.querySelector('.modal');
const closeModal = () => {
  modal.classList.remove('visible');
}
let closeButton = document.querySelector('.closeModal');
closeButton.addEventListener('click', closeModal);
document.addEventListener('keyup', function(e) {
  if (e.keyCode == 27) {
    closeModal();
  }
});
let otherClicks = (event) => {
  if (document.querySelector('.modal').contains(event.target)) {
    return false;
  } else {
    closeModal();
    window.removeEventListener('click', otherClicks);
  }
};
window.addEventListener('click', otherClicks);
const anchorLink = document.querySelector('a[data-role="createLink"]');

anchorLink.addEventListener('click', () => {
  modal.classList.add('visible');
  window.savedSel = saveSelection();
  document.urlForm.urlField.value="";
  document.urlForm.urlField.focus();
})


// Save selected text when URL modal opens. From http://stackoverflow.com/questions/5605401/insert-link-in-contenteditable-element
function saveSelection() {
    if (window.getSelection) {
        sel = window.getSelection();
        if (sel.getRangeAt && sel.rangeCount) {
            var ranges = [];
            for (var i = 0, len = sel.rangeCount; i < len; ++i) {
                ranges.push(sel.getRangeAt(i));
            }
            return ranges;
        }
    } else if (document.selection && document.selection.createRange) {
        return document.selection.createRange();
    }
    return null;
}

function restoreSelection(savedSel) {
    if (savedSel) {
        if (window.getSelection) {
            sel = window.getSelection();
            sel.removeAllRanges();
            for (var i = 0, len = savedSel.length; i < len; ++i) {
                sel.addRange(savedSel[i]);
            }
        } else if (document.selection && savedSel.select) {
            savedSel.select();
        }
    }
}

let urlForm = document.querySelector('.urlForm');

urlForm.addEventListener('submit',(e) => {
  let urlValue = urlForm.querySelector('.url').value;
  restoreSelection(window.savedSel);
    document.execCommand("CreateLink", false, urlValue);
  closeModal();
  e.preventDefault();
})

function getSelectionParentElement() {
    var parentEl = null, sel;
    if (window.getSelection) {
        sel = window.getSelection();
        if (sel.rangeCount) {
            parentEl = sel.getRangeAt(0).commonAncestorContainer;
            if (parentEl.nodeType != 1) {
                parentEl = parentEl.parentNode;
            }
        }
    } else if ( (sel = document.selection) && sel.type != "Control") {
        parentEl = sel.createRange().parentElement();
    }
    return parentEl;
}