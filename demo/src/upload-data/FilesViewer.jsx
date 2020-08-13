import React from "react";
import { RicosViewer, empty } from "../text-viewer";
import update from "immutability-helper";

export function createFileContent(url, filename) {
  let entityMap = Object.assign({}, empty.entityMap);
  let data = { url };
  if (filename) {
    data.name = filename;
    const fileNameParts = filename.split(".");
    data.type = fileNameParts[fileNameParts.length - 1];
  }
  entityMap = update(entityMap, {
    "0": { data: { $merge: data } },
  });
  return update(empty, { entityMap: { $merge: entityMap } });
}

export function FilesViewer(props) {
  console.log(props.filesContent);
  return props.filesContent.map((content, index) => {
    return (
      <div key={index}>
        <RicosViewer contentState={content} />
      </div>
    );
  });
}
