   function changeTab(tabIndex) {
      var tabButtons = document.getElementsByClassName('tab-button');
      var tabContents = document.getElementsByClassName('tab-content');
      if (tabIndex==0){
        $("#newdiv").hide();
      }
      else{
        if ($('#mytab').is(':visible')) {
        // #mytab is shown, do nothing
      } else {
        // #mytab is not shown, show #newdiv
        $("#newdiv").show();
      }

      }
      for (var i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove('active');
        tabContents[i].classList.remove('active');
      }

      tabButtons[tabIndex].classList.add('active');
      tabContents[tabIndex].classList.add('active');
    }
    $(document).ready(function() {
      $("#newdiv").hide();
  $("#submitData").click(function() {
    var name = $("#name").val();
    var dob = $("#dob").val();
    var adhar = $("#adhar").val();
    var nationality = $("#nationality").val();
    var state = $("#state").val();
    var address = $("#address").val();
    var ipc = $("#ipc").val();
    var jailType = $("#jail-type").val();
    var jailLocation = $("#jail-location").val();
    var jailCount = $("#jail-count").val();

    var data = {
      name: name,
      dob: dob,
      adhar: adhar,
      nationality: nationality,
      state: state,
      address: address,
      ipc: ipc,
      jailType: jailType,
      jailLocation: jailLocation,
      jailCount: jailCount
    };

    $.ajax({
      type: "POST",
      url: "/add",
      data: JSON.stringify(data),
      contentType: "application/json",
      success: function(response) {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        console.log("Success:", response);
        $("#errorMessage").hide();

        $("#successMessage").show();
      },
      error: function(error) {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        console.log("Error:", error);
        $("#errorMessage").show();
        $("#successMessage").hide();
      }
    });
  });
});
$(document).ready(function() {
  $('#search-bar').on('input', function() {
    var searchQuery = $(this).val();

    if (searchQuery === "") {
      $("#preview-results").hide();
    } else {
      $("#preview-results").show();

      $.post('/getData', { searchQuery: searchQuery }, function(data) {
        displayPreviewResults(data);
      });
    }
  });


  function displaySearchResults(results) {
    var searchResultsContainer = $('#search-results');
    searchResultsContainer.empty();

    $.each(results, function(index, result) {
      var searchResultItem = $('<div>').addClass('search-result-item');


      searchResultItem.append("<button class='edit-button' onclick='func("+result.uid+")'>Edit</button>")

      searchResultItem.append('<h2>' + result.name + '</h2>');
      searchResultItem.append('<p><strong>UID:</strong> ' + result.uid + '</p>');
      searchResultItem.append('<p><strong>Date of Birth:</strong> ' + result.dob + '</p>');
      searchResultItem.append('<p><strong>Adhar:</strong> ' + result.adhar + '</p>');
      searchResultItem.append('<p><strong>Nationality:</strong> ' + result.nationality + '</p>');
      searchResultItem.append('<p><strong>State:</strong> ' + result.state + '</p>');
      searchResultItem.append('<p><strong>Address:</strong> ' + result.address + '</p>');
      searchResultItem.append('<p><strong>IPC Section:</strong> ' + result.ipc_section + '</p>');
      searchResultItem.append('<p><strong>Jail Type:</strong> ' + result.jail_type + '</p>');
      searchResultItem.append('<p><strong>Jail Location:</strong> ' + result.jail_location + '</p>');
      searchResultItem.append('<p><strong>Times in Jail:</strong> ' + result.times_in_jail + '</p>');

      searchResultsContainer.append(searchResultItem);
    });
  }
});
    function func(uid){
      //show the updation form.here
      //and call the update(uid) to update
    }

    // Function for submit button click event
    function updation(uid) {
    var name = $("#name1").val();
    var dob = $("#dob1").val();
    var adhar = $("#adhar1").val();
    var nationality = $("#nationality1").val();
    var state = $("#state1").val();
    var address = $("#address1").val();
    var ipc = $("#ipc1").val();
    var jailType = $("#jail-type1").val();
    var jailLocation = $("#jail-location1").val();
    var jailCount = $("#jail-count1").val();

    var data = {
      uid:uid,
      name: name,
      dob: dob,
      adhar: adhar,
      nationality: nationality,
      state: state,
      address: address,
      ipc: ipc,
      jailType: jailType,
      jailLocation: jailLocation,
      jailCount: jailCount
    };

    $.ajax({
      type: "POST",
      url: "/update",
      data: JSON.stringify(data),
      contentType: "application/json",
      success: function(response) {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        console.log("Success:", response);
        $("#errorMessage1").hide();

        $("#successMessage1").show();
      },
      error: function(error) {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        console.log("Error:", error);
        $("#errorMessage1").show();
        $("#successMessage1").hide();
      }
    });
    }

    
    function updateJailDropdown() {
      var jailType = document.getElementById("jail-type").value;
      var jailLocationField = document.getElementById("jail-location-field");
      var jailLocationDropdown = document.getElementById("jail-location");

      if (jailType === "central") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Poojappura,Thiruvananthapuram">Central Prison & Correctional Home, Poojappura,Thiruvananthapuram</option>
          <option value="Viyyur, Thrissur">Central Prison & Correctional Home, Viyyur, Thrissur</option>
          <option value="Pallikkunnu, Kannur">Central Prison & Correctional Home, Pallikkunnu, Kannur</option>
        `;
      } else if (jailType === "district") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Thiruvananthapuram (Poojappura)">District Jail Thiruvananthapuram (Poojappura)</option>
          <option value="Kollam">District Jail Kollam</option>
          <option value="Pathanamthitta">District Jail Pathanamthitta</option>
          <option value="Alappuzha">District Jail Alappuzha</option>
          <option value="Kottayam">District Jail Kottayam</option>
          <option value="Ernakulam">District Jail Ernakulam</option>
          <option value="Idukki (Muttom)">District Jail Idukki (Muttom)</option>
          <option value="Thrissur (Viyyur)">District Jail Thrissur (Viyyur)</option>
          <option value="Palakkad (Malampuzha)">District Jail Palakkad (Malampuzha)</option>
          <option value="Kozhikode">District Jail Kozhikode</option>
          <option value="Kannur">District Jail Kannur</option>
          <option value="Wayanad (Mananthavady)">District Jail Wayanad (Mananthavady)</option>
          <option value="Kasaragod (Hosdurg)">District Jail Kasaragod (Hosdurg)</option>
        `;
      } else if (jailType === "sub-jail") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Attingal">Attingal</option>
          <option value="Meenachil">Meenachil</option>
          <option value="Peerumade">Peerumade</option>
          <option value="Mattancherry">Mattancherry</option>
          <option value="Ernakulam">Ernakulam</option>
          <option value="Aluva">Aluva</option>
          <option value="Chavakkad">Chavakkad</option>
          <option value="Viyyur">Viyyur</option>
          <option value="Alathur">Alathur</option>
          <option value="Ottappalam">Ottappalam</option>
          <option value="Perinthalmanna">Perinthalmanna</option>
          <option value="Ponnani">Ponnani</option>
          <option value="Tirur">Tirur</option>
          <option value="Koyilandy">Koyilandy</option>
          <option value="Vatakara">Vatakara</option>
          <option value="Kannur">Kannur</option>
        `;
      } else {
        jailLocationField.style.display = "none";
      }
    }


     function updateJailDropdown2() {
      var jailType = document.getElementById("new-jail-type").value;
      var jailLocationField = document.getElementById("new-jail-location-field");
      var jailLocationDropdown = document.getElementById("new-jail-location");

      if (jailType === "central") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Poojappura,Thiruvananthapuram">Central Prison & Correctional Home, Poojappura,Thiruvananthapuram</option>
          <option value="Viyyur, Thrissur">Central Prison & Correctional Home, Viyyur, Thrissur</option>
          <option value="Pallikkunnu, Kannur">Central Prison & Correctional Home, Pallikkunnu, Kannur</option>
        `;
      } else if (jailType === "district") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Thiruvananthapuram (Poojappura)">District Jail Thiruvananthapuram (Poojappura)</option>
          <option value="Kollam">District Jail Kollam</option>
          <option value="Pathanamthitta">District Jail Pathanamthitta</option>
          <option value="Alappuzha">District Jail Alappuzha</option>
          <option value="Kottayam">District Jail Kottayam</option>
          <option value="Ernakulam">District Jail Ernakulam</option>
          <option value="Idukki (Muttom)">District Jail Idukki (Muttom)</option>
          <option value="Thrissur (Viyyur)">District Jail Thrissur (Viyyur)</option>
          <option value="Palakkad (Malampuzha)">District Jail Palakkad (Malampuzha)</option>
          <option value="Kozhikode">District Jail Kozhikode</option>
          <option value="Kannur">District Jail Kannur</option>
          <option value="Wayanad (Mananthavady)">District Jail Wayanad (Mananthavady)</option>
          <option value="Kasaragod (Hosdurg)">District Jail Kasaragod (Hosdurg)</option>
        `;
      } else if (jailType === "sub-jail") {
        jailLocationField.style.display = "block";
        jailLocationDropdown.innerHTML = `
          <option value="Attingal">Attingal</option>
          <option value="Meenachil">Meenachil</option>
          <option value="Peerumade">Peerumade</option>
          <option value="Mattancherry">Mattancherry</option>
          <option value="Ernakulam">Ernakulam</option>
          <option value="Aluva">Aluva</option>
          <option value="Chavakkad">Chavakkad</option>
          <option value="Viyyur">Viyyur</option>
          <option value="Alathur">Alathur</option>
          <option value="Ottappalam">Ottappalam</option>
          <option value="Perinthalmanna">Perinthalmanna</option>
          <option value="Ponnani">Ponnani</option>
          <option value="Tirur">Tirur</option>
          <option value="Koyilandy">Koyilandy</option>
          <option value="Vatakara">Vatakara</option>
          <option value="Kannur">Kannur</option>
        `;
      } else {
        jailLocationField.style.display = "none";
      }
    }
    $(document).ready(function() {
  $("#searchFor").click(function() {
    var name = $("#new-name").val();
    var dob = $("#new-dob").val();
    var adhar = $("#new-adhar").val();
    var nationality = $("#new-nationality").val();
    var state = $("#new-state").val();
    var address = $("#new-address").val();
    var ipc = $("#new-ipc").val();
    var jailType = $("#new-jail-type").val();
    var jailLocation = $("#new-jail-location").val();
    var jailCount = $("#new-jail-count").val();

    var data = {
      name: name,
      dob: dob,
      adhar: adhar,
      nationality: nationality,
      state: state,
      address: address,
      ipc: ipc,
      jailType: jailType,
      jailLocation: jailLocation,
      jailCount: jailCount
    };

    $.ajax({
      url: "/search",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: function(response) {
        // Handle the response from the server
      },
      error: function(error) {
        // Handle any errors that occurred during the request
      }
    });
  });
});