import React, { Component } from "react";
import WktItemSingle from "./wkt-item-single";
import { Container } from "react-bootstrap";
import { connect } from "react-redux";
import { DragDropContext, Droppable } from "react-beautiful-dnd";
import { apply_ordering, move_arr_item } from "../utils/utils";

class DeepMITs extends Component {
  state = { ordered: [] };

  componentDidMount() {
    this.setState({ ordered: this.props.items });
  }

  componentDidUpdate() {
    const { ordered } = this.state;
    const new_order = apply_ordering(ordered, this.props.items);
    if (new_order !== this.state.ordered) this.setState({ ordered: new_order });
  }

  handle_drag = (result) => {
    const { source, destination, draggableId } = result;
    const { ordered } = this.state;
    if (
      !destination ||
      source.droppableId !== destination.droppableId ||
      source.index === destination.index
    )
      return;
    const src_idx = ordered.indexOf(draggableId);
    const dest_idx = ordered.indexOf(ordered[destination.index]);
    const new_order = move_arr_item(ordered, src_idx, dest_idx);
    this.setState({ ordered: new_order });
  };

  render() {
    const { items } = this.props.workette;
    const { ordered } = this.state;
    return (
      <Container fluid className="m-0 p-0">
        {this.props.items && this.props.items.length > 0 && (
          <div>
            <br />
            {this.props.label}
          </div>
        )}
        <DragDropContext onDragEnd={this.handle_drag}>
          <Droppable droppableId={this.props.w_id}>
            {(provided) => (
              <div {...provided.droppableProps} ref={provided.innerRef}>
                {this.props.items.map((i, idx) => (
                  <React.Fragment key={i}>
                    {
                      <WktItemSingle
                        item={items[i]}
                        index={idx}
                        is_workset={false}
                        color={this.props.color}
                      />
                    }
                  </React.Fragment>
                ))}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        </DragDropContext>
      </Container>
    );
  }
}

//Connect this component to store.session
const map_state = (state) => ({
  workette: state.workette,
});
export default connect(map_state)(DeepMITs);