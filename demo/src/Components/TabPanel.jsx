import React from "react";
import PropTypes from "prop-types";
import Box from "@material-ui/core/Box";

export default function TabPanel(props) {
  const { children, currentTabIndex, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={currentTabIndex !== index}
      id={`tabpanel-${index}`}
      aria-labelledby={`tab-${index}`}
      {...other}
    >
      {currentTabIndex === index && <Box p={3}>{children}</Box>}
    </div>
  );
}

TabPanel.propTypes = {
  currentTabIndex: PropTypes.number.isRequired,
  index: PropTypes.number.isRequired,
  children: PropTypes.any,
};
