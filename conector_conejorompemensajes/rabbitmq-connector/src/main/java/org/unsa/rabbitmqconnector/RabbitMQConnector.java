package org.unsa.rabbitmqconnector;

import java.util.logging.Logger;

import org.bonitasoft.engine.connector.AbstractConnector;
import org.bonitasoft.engine.connector.ConnectorException;
import org.bonitasoft.engine.connector.ConnectorValidationException;

import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.ConnectionFactory;

public class RabbitMQConnector extends AbstractConnector {

    @Override
    protected void executeBusinessLogic() throws ConnectorException {
        try {
            // Get input parameters
            String host = (String) getInputParameter("host");
            int port = Integer.parseInt((String) getInputParameter("port"));
            String username = (String) getInputParameter("username");
            String password = (String) getInputParameter("password");
            String queueName = (String) getInputParameter("queueName");
            String message = (String) getInputParameter("message");
            
            // Create connection factory
            ConnectionFactory factory = new ConnectionFactory();
            factory.setHost(host);
            factory.setPort(port);
            factory.setUsername(username);
            factory.setPassword(password);
            
            // Create connection and channel
            try (Connection connection = factory.newConnection();
                 Channel channel = connection.createChannel()) {
                
                // Declare the queue
                channel.queueDeclare(queueName, false, false, false, null);
                
                // Publish the message
                channel.basicPublish("", queueName, null, message.getBytes());
                
                // Set output parameter
                setOutputParameter("success", true);
            }
        } catch (Exception e) {
            throw new ConnectorException(e);
        }
    }

    @Override
    public void validateInputParameters() throws ConnectorValidationException {
        // Validate required parameters
        requireNotNullOrEmptyInputParameter("host");
        requireNotNullOrEmptyInputParameter("port");
        requireNotNullOrEmptyInputParameter("queueName");
        requireNotNullOrEmptyInputParameter("message");
    }
    
    private void requireNotNullOrEmptyInputParameter(String parameterName) throws ConnectorValidationException {
        Object parameter = getInputParameter(parameterName);
        if (parameter == null || parameter.toString().trim().isEmpty()) {
            throw new ConnectorValidationException(String.format("Parameter '%s' is required", parameterName));
        }
    }
}