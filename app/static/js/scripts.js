// Example script to handle form submissions and API requests
document.addEventListener('DOMContentLoaded', function() {
  const employeeForm = document.getElementById('employee-form');
  employeeForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(employeeForm);
      fetch('/employees', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          // Handle response
          console.log(data);
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });

  // Similar event listeners for other forms (payroll, timesheet, vacations)
});
