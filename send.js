  var TeleSignSDK = require('telesignsdk');

  const customerId = "DADE1E06-9E95-4D3D-B99E-FE4349B7B8AF";
  const apiKey = "+HXY3sboYAzZcfE4CNguU8xSppXgU9l/3r8XVQXetoCZRYCqdmxslggXBBTtcMgXuajzb/bo15MWYxkUn6de2A==";
  const rest_endpoint = "https://rest-api.telesign.com";
  const timeout = 10*1000; // 10 secs

  const client = new TeleSignSDK( customerId,
      apiKey,
      rest_endpoint,
      timeout // optional
      // userAgent
  );

  const phoneNumber = "+212616952526";
  const message = "You're scheduled for a dentist appointment at 2:30PM.";
  const messageType = "ARN";

  console.log("## MessagingClient.message ##");

  function messageCallback(error, responseBody) {
      if (error === null) {
          console.log(`Messaging response for messaging phone number: ${phoneNumber}` +
              ` => code: ${responseBody['status']['code']}` +
              `, description: ${responseBody['status']['description']}`);
      } else {
          console.error("Unable to send message. " + error);
      }
  }
  client.sms.message(messageCallback, phoneNumber, message, messageType);
  