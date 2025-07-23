package org.unsa.rabbitmqconnector;

import org.bonitasoft.engine.connector.ConnectorException;
import org.bonitasoft.engine.connector.ConnectorValidationException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

class RabbitMQConnectorTest {

    RabbitMQConnector connector;

    @BeforeEach
    void setUp() {
        connector = new RabbitMQConnector();
    }

    @Test
    void should_throw_exception_if_mandatory_input_is_missing() {
        assertThrows(ConnectorValidationException.class, () ->
                connector.validateInputParameters()
        );
    }

    @Test
    void should_throw_exception_if_mandatory_input_is_empty() {
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("host", "");
        parameters.put("port", "");
        parameters.put("queueName", "");
        parameters.put("message", "");
        connector.setInputParameters(parameters);
        assertThrows(ConnectorValidationException.class, () ->
                connector.validateInputParameters()
        );
    }

    @Test
    void should_throw_exception_if_host_is_missing() {
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("port", "5672");
        parameters.put("queueName", "test");
        parameters.put("message", "hello");
        connector.setInputParameters(parameters);
        assertThrows(ConnectorValidationException.class, () ->
                connector.validateInputParameters()
        );
    }

    @Test
    void should_send_message_to_queue_with_valid_input() throws ConnectorValidationException, ConnectorException {
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("host", "localhost");
        parameters.put("port", "5672");
        parameters.put("username", "guest");
        parameters.put("password", "guest");
        parameters.put("queueName", "testQueue");
        parameters.put("message", "hello");

        connector.setInputParameters(parameters);
        
        connector.validateInputParameters(); // Asegura que los parámetros sean válidos
        
        Map<String, Object> outputs = connector.execute(); // Llama al conector

        assertThat(outputs).containsEntry("success", true); // Verifica que fue exitoso
    }
}
