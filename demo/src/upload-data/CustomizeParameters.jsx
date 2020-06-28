import React, { Component } from "react";
import {
  Button,
  Paper,
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  FormLabel,
  TextField,
} from "@material-ui/core";

export default class CustomizeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      resolution: "BySession",
      eventSpeaker: "event_speaker",
      measures: [],
      session: "session_number",
      dyad: "dyad",
    };
  }

  convertMeasuresToString = () => {
    let result = "";
    this.state.measures.forEach((measure) => (result += measure + " "));
    return result;
  };

  renderParametersForm = () => {
    return (
      <FormControl>
        <FormLabel>Data Parameters</FormLabel>
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
          defaultValue={this.convertMeasuresToString()}
          margin="normal"
          onChange={(event) =>
            this.setState({ measures: event.target.value.split(" ") })
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
            onChange={(event) => this.setState({ session: event.target.value })}
          />
        )}
      </FormControl>
    );
  };

  onClose() {
    const { eventSpeaker, measures, session, dyad, resolution } = this.state;
    this.props.onClose({
      eventSpeaker,
      measures,
      dyad,
      session: resolution === "BySession" && session,
    });
  }

  render() {
    return (
      <Paper>
        {this.renderParametersForm()}
        <Button
          onClick={() => this.onClose()}
          variant="contained"
          color="primary"
          component="span"
        >
          Save And Close
        </Button>
      </Paper>
    );
  }
}
