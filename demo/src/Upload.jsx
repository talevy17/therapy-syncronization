import React, { Component } from "react";

export default class Upload extends Component {
  handleFileUpload = (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    data.append("filename", this.fileName.value);

    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      console.log(response);
    });
  };

  render() {
    return (
      <form onSubmit={this.handleFileUpload}>
        <div>
          <input
            ref={(ref) => {
              this.uploadInput = ref;
            }}
            type="file"
          />
        </div>
        <div>
          <input
            ref={(ref) => {
              this.fileName = ref;
            }}
            type="text"
            placeholder="Enter the desired name of file"
          />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
      </form>
    );
  }
}
