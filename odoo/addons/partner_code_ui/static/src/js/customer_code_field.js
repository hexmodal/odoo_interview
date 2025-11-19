/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

const { Component } = owl;

export class CustomerCodeField extends Component {
    // TODO: implement validation + RPC + messages as needed.
    onInput(ev) {
        const value = ev.target.value || "";
        if (this.props.update) {
            this.props.update(value);
        }
    }
}

CustomerCodeField.template = "partner_code_ui.CustomerCodeField";
CustomerCodeField.props = {
    ...standardFieldProps,
};
CustomerCodeField.supportedTypes = ["char"];

registry.category("fields").add("customer_code", CustomerCodeField);
