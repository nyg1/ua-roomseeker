// Helper file for some of the database interactions.

// Imports.
const express = require('express');
const mariadb = require('mariadb');

// Options for standard database connection.
exports.standardOptions = {
  database: 'roomseeker',
  host: 'localhost',
  user: 'site_user',
  password: 'seeker'
};

/**
 * General query function to handle database queries.
 * It sends result directly to the client, so a response stream needs
 * to be provided.
 * @param sql (string): SQL query to execute.
 * @param opt (Object): Database options list.
 * @param callback (function): Callback function, to send result to.
 * @param args (Array): The arguments to give the query.
 */
exports.query = (sql, opt, callback, args) => {
    let argv = args || [];
  
    // Immediately throw an error if options, callback, or sql are not provided.
    if (sql === undefined || opt === undefined || callback === undefined) {
      callback({ badRequest: true });
    } else {
  
      // Establish a connection and execute the query.
      mariadb.createConnection(opt).then(conn => {
        conn.query(sql, argv).then(result => {
          callback(result);
  
          // Close the connection.
          conn.end().then(() => {}).catch(err => console.log(err));
        }).catch(err => callback(err));
      }).catch(err => callback(err));
    }
  }
  
  /**
   * Function to handle simple GET requests.
   * @param res (Respose): Response for the user.
   * @param sql (string): SQL query to make.
   * @param opt (Object): Database connection options.
   * @param args (Array): The arguments to give the query.
   */
  exports.simpleGET = (res, sql, opt, args) => {
    // Handle undefined response.
    if (res === undefined) {
      throw new Error('Error: undefined Response object');
    }
  
    // Set response type to be json.
    res.type('application/json');
  
    this.query(sql, opt, (result) => {
      // Return the appropriate response.
      if (result['badRequest'] !== undefined) res.send({ message: 'Bad request, missing arguments.' });
      else if (result['errno'] !== undefined) res.send({ message: this.errorMsg(result['errno']) });
      else res.send(result);
    }, args);
  };
  
  /**
   * Function to handle simple POST requests.
   * @param res (Respose): Response for the user.
   * @param sql (string): SQL query to make.
   * @param opt (Object): Database connection options.
   * @param args (Array): The arguments to give the query.
   * @param successMsg (string): Success message to send to client.
   */
  exports.simplePOST = (res, sql, opt, args, successMsg) => {
    // Handle undefined response.
    if (res === undefined) {
      throw new Error('Error: undefined Response object');
    }
  
    // Set response type to be json.
    res.type('application/json');
  
    this.query(sql, opt, (result) => {
      // Return the appropriate response.
      if (result['badRequest'] !== undefined) res.send({ message: 'Bad request, missing arguments.' });
      else if (result['errno'] !== undefined) res.send({ message: this.errorMsg(result['errno']) });
      else if (successMsg !== undefined) res.send({ message: successMsg });
    }, args);
  };
  
  /**
   * Return an appropriate error message for the client depending on
   * the error number of a given query.
   * @param errno (number): The error number of the query.
   * @return msg (string): Error message.
   */
  exports.errorMsg = (errno) => {
    let msg = 'There was an error when making the request.';
  
    if (errno === 1045) msg = 'Could not connect to the database.';
    else if (errno === 1062) msg = 'That ID is already in the database.';
    else if (errno === 1146) msg = 'Invalid query.';
  
    return msg;
  }
  
