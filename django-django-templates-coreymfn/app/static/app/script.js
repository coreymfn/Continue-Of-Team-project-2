const membersButton = document.getElementById("members-button");
const memberList = document.getElementById("member-list");

membersButton.addEventListener("click", function () {
    if (memberList.hidden) {
        memberList.hidden = false;
        membersButton.textContent = "Hide Members";
        membersButton.setAttribute("aria-expanded", "true");
    } else {
        memberList.hidden = true;
        membersButton.textContent = "See Members";
        membersButton.setAttribute("aria-expanded", "false");
    }
});