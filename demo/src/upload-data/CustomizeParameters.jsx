import React, { Component } from "react";
import {
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  TextField,
} from "@material-ui/core";

import { SettingsModal } from "../Components";

export default class CustomizeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      resolution: "BySession",
      eventSpeaker: "",
      measures: [],
      speakers: [],
      transcription: "",
      dyad: "",
      key: "",
      numOfWords: null,
    };
  }

  convertListToString = (list) => {
    let result = "";
    list.forEach((item) => (result += item + " "));
    return result;
  };

  renderParametersForm = () => {
    return (
      <FormControl>
        <TextField
          label="Transcription Key"
          id="transcription-hard-key"
          defaultValue={this.state.key}
          margin="normal"
          onChange={(event) => this.setState({ key: event.target.value })}
        />
        <TextField
          label="Event Speaker"
          id="event-speaker"
          defaultValue={this.state.eventSpeaker}
          margin="normal"
          onChange={(event) =>
            this.setState({ eventSpeaker: event.target.value })
          }
        />
        <TextField
          label="Measures"
          id="measuers"
          defaultValue={this.convertListToString(this.state.measures)}
          margin="normal"
          onChange={(event) =>
            this.setState({ measures: event.target.value.split(" ") })
          }
        />
        <TextField
          label="Speakers"
          id="speakers"
          defaultValue={this.convertListToString(this.state.speakers)}
          margin="normal"
          onChange={(event) =>
            this.setState({ speakers: event.target.value.split(" ") })
          }
        />
        <TextField
          label="Number of words"
          id="num-of-words"
          defaultValue={this.state.numOfWords}
          margin="normal"
          onChange={(event) =>
            this.setState({ numOfWords: event.target.value })
          }
        />
        <RadioGroup
          name={"Conversation Resolution"}
          onChange={(event) =>
            this.setState({ resolution: event.target.value })
          }
          defaultValue={this.state.resolution}
        >
          <FormControlLabel
            value={"BySession"}
            control={<Radio />}
            label={"By Session"}
          />
          <FormControlLabel
            value={"ByDyad"}
            control={<Radio />}
            label={"By Dyad"}
          />
        </RadioGroup>
        <TextField
          label="Dyad Column"
          id="by-dyad"
          defaultValue={this.state.dyad}
          margin="normal"
          onChange={(event) => this.setState({ dyad: event.target.value })}
        />
        {this.state.resolution === "BySession" && (
          <TextField
            label="Session Column"
            id="by-session"
            defaultValue={this.state.transcription}
            margin="normal"
            onChange={(event) =>
              this.setState({ transcription: event.target.value })
            }
          />
        )}
      </FormControl>
    );
  };

  onClose() {
    const {
      eventSpeaker,
      measures,
      transcription,
      dyad,
      resolution,
      speakers,
      key,
      numOfWords,
    } = this.state;
    this.props.onClose({
      eventSpeaker,
      measures,
      speakers,
      dyad,
      transcription: resolution === "BySession" && transcription,
      key,
      numOfWords,
    });
  }

  render() {
    return (
      <SettingsModal
        isOpen={this.props.isOpen}
        onClose={() => this.onClose()}
        title={"Data Parameters"}
      >
        {this.renderParametersForm()}
      </SettingsModal>
    );
  }
}
