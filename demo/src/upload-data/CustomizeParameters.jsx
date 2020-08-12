import React, { Component } from "react";
import {
  Paper,
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
      eventSpeaker: "event_speaker",
      measures: [],
      speakers: [],
      transcription: "session_number",
      dyad: "dyad",
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
            defaultValue={this.state.session}
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
    } = this.state;
    this.props.onClose({
      eventSpeaker,
      measures,
      speakers,
      dyad,
      transcription: resolution === "BySession" && transcription,
    });
  }

  render() {
    return (
      <SettingsModal
        isOpen={this.props.isOpen}
        onClose={() => this.onClose()}
        title={"Data Parameters"}
        modalBody={this.renderParametersForm}
      />
    );
  }
}
